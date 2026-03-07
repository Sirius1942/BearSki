# BearSki 2.0 原型

## 核心特性

### 1. 三要素模型
- **业务模型** (models/)
- **数据表** (testdata/)
- **关键字** (keywords/)

### 2. 动态数据函数
数据表支持函数：
- `${now()}` - 当前时间
- `${today()}` - 今天日期
- `${random_str(5)}` - 随机字符串
- `${random_int(1,100)}` - 随机数字

### 3. Session 共享
DB/REST/UI 驱动共享 session 和数据

---

## 示例

### 数据表 (testdata.xlsx)
```
| DataID | username              | timestamp      |
|--------|-----------------------|----------------|
| admin  | admin                 | ${now()}       |
| test1  | test_${random_str(5)} | ${today()}     |
```

### 业务模型 (models/api_test.yaml)
```yaml
model:
  name: API 测试
  flow:
    - step: 发送请求
      keyword: rest.get
    - step: 验证状态码
      keyword: rest.assert_status
```

### 测试用例 (testcases/test_api.yaml)
```yaml
testcase:
  name: API 测试
  model: api_test
  data: testdata.xlsx::login_data::admin
```

---

## 运行
```bash
cd bearski2
python main.py
```
