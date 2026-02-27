# Task 7: 退出码验证报告

## 问题澄清

用户反馈退出码为 0 的原因是使用了管道命令：
```bash
python3 validate_layout.py /tmp/bad-margin.html 2>&1 | grep "FAIL"
echo "EXIT CODE: $?"
```

在这个命令中，`$?` 捕获的是 **grep 的退出码**（找到匹配返回0），而非 Python 脚本的退出码。

## 正确的测试方法

### 方法1: 捕获脚本退出码
```bash
python3 validate_layout.py /tmp/bad-margin.html > /dev/null 2>&1
echo "EXIT CODE: $?"
```

### 方法2: 同时捕获输出和退出码
```bash
OUTPUT=$(python3 validate_layout.py /tmp/bad-margin.html 2>&1)
EXIT_CODE=$?
echo "$OUTPUT" | grep "FAIL"
echo "EXIT CODE: $EXIT_CODE"
```

## 验证结果

### 测试1: 合规模板（应该退出码0）
```bash
$ python3 scripts/validate_layout.py assets/template-single-column.html > /dev/null 2>&1
$ echo $?
0
✅ PASS
```

### 测试2: 错误边距（应该退出码1）
```bash
$ python3 scripts/validate_layout.py /tmp/bad-margin.html > /dev/null 2>&1
$ echo $?
1
✅ PASS
```

### 测试3: 错误边距 + 输出验证
```bash
$ OUTPUT=$(python3 scripts/validate_layout.py /tmp/bad-margin.html 2>&1)
$ EXIT_CODE=$?
$ echo "$OUTPUT" | grep "FAIL: page_margin_top"
FAIL: page_margin_top — 未找到 margin-top: 3.3cm
✅ 输出包含 FAIL: page_margin_top

$ echo $EXIT_CODE
1
✅ 退出码正确
```

### 测试4: --check-mapping（应该退出码0）
```bash
$ python3 scripts/validate_layout.py --check-mapping references/style-mapping.md > /dev/null 2>&1
$ echo $?
0
✅ PASS
```

## 脚本逻辑验证

### 主函数退出逻辑（行 301-306）
```python
# 最终判定
if failed == 0:
    print("✅ 所有规则通过！")
    sys.exit(0)
else:
    print(f"❌ 有 {failed} 条规则失败！")
    sys.exit(1)
```

### --check-mapping 退出逻辑（行 266-267）
```python
md_file = sys.argv[2]
success = check_mapping(md_file)
sys.exit(0 if success else 1)
```

### check_mapping 函数返回值（行 214-246）
```python
def check_mapping(md_file):
    """检验 style-mapping.md 是否包含所有必填字段"""
    required_fields = [
        "Times New Roman", "3.3cm", "17.9pt", "14.5pt",
        "36 字", "小4", "5号", "1号"
    ]
    
    # ... 读取文件 ...
    
    missing = []
    for field in required_fields:
        if field not in content:
            missing.append(field)
    
    if missing:
        print(f"❌ 映射文件缺少必填字段:")
        for field in missing:
            print(f"   - missing size mapping: {field}")
        return False  # 返回 False → sys.exit(1)
    else:
        print(f"✅ 映射文件包含所有必填字段")
        for field in required_fields:
            print(f"   ✓ {field}")
        return True  # 返回 True → sys.exit(0)
```

## 结论

✅ 脚本退出码逻辑**完全正确**：
- 合规 HTML → 退出码 0
- 错误 HTML → 退出码 1
- 映射完整 → 退出码 0
- 映射缺失 → 退出码 1

✅ 所有预期结果已达成：
- `run_all()` 正确统计 failed 数量
- 主函数末尾：`sys.exit(0 if failed == 0 else 1)`
- `--check-mapping` 模式在发现缺失字段时 `sys.exit(1)`

用户之前观察到退出码为 0 是因为使用了管道命令 `| grep "FAIL"; echo $?`，`$?` 捕获的是 grep 的退出码而非脚本本身的退出码。使用正确的测试方法后，所有退出码均符合预期。
