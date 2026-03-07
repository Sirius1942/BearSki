# BearSki 2.0 示例

## 动态数据函数

### 支持的函数
- `${now()}` - 当前时间（2026-03-07 08:05:30）
- `${today()}` - 今天日期（2026-03-07）
- `${timestamp()}` - Unix 时间戳
- `${random_str(5)}` - 随机字符串（5位）
- `${random_int(1,100)}` - 随机整数（1-100）
- `${random_email()}` - 随机邮箱

### Excel 格式示例
```
| DataID | username              | timestamp  |
|--------|-----------------------|------------|
| admin  | admin                 | ${now()}   |
| test1  | test_${random_str(5)} | ${today()} |
```

**运行时动态计算：**
```
admin -> timestamp: "2026-03-07 08:05:30"
test1 -> username: "test_aBcDe", timestamp: "2026-03-07"
```

### JSON 格式示例
```json
[
  {
    "DataID": "admin",
    "username": "admin",
    "email": "${random_email()}",
    "timestamp": "${now()}"
  }
]
```

**运行时动态计算：**
```json
{
  "username": "admin",
  "email": "test_1234@example.com",
  "timestamp": "2026-03-07 08:05:30"
}
```

---

## 测试用例示例

### 使用 Excel 数据
```yaml
testcase:
  model: api_test
  data: testdata.xlsx::login_data::admin
```

### 使用 JSON 数据
```yaml
testcase:
  model: api_test
  data: testdata.json::login_data::admin
```

---

**棘轮签名** 🏥
