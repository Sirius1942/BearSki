"""BearSki 2.0 主程序"""
from core.executor import Executor

if __name__ == "__main__":
    executor = Executor()
    executor.run_testcase("dsl/testcases/test_api.yaml")
    print("✅ 测试执行完成")
