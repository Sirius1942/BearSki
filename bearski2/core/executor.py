"""执行引擎"""
import yaml
from .session import TestSession
from .data_loader import DataLoader
from ..drivers.rest_driver import RESTDriver
from ..drivers.ui_driver import UIDriver

class Executor:
    def __init__(self):
        self.session = TestSession()
        self.data_loader = DataLoader()
        self.drivers = {
            'rest': RESTDriver(self.session),
            'ui': UIDriver(self.session),
        }
    
    def run_testcase(self, testcase_file):
        with open(testcase_file) as f:
            testcase = yaml.safe_load(f)
        
        model_file = f"dsl/models/{testcase['model']}.yaml"
        with open(model_file) as f:
            model = yaml.safe_load(f)
        
        # 使用统一的 load 接口，支持 Excel 和 JSON
        data_path = testcase['data']
        test_data = self.data_loader.load(f"dsl/testdata/{data_path}")
        
        print(f"📊 加载的测试数据: {test_data}")
        
        for step in model['model']['flow']:
            self._execute_step(step, test_data)
    
    def _execute_step(self, step, data):
        keyword = step['keyword']
        driver_name, action = keyword.split('.')
        driver = self.drivers[driver_name]
        params = self._resolve_params(step.get('params', {}), data)
        getattr(driver, action)(**params)
    
    def _resolve_params(self, params, data):
        result = {}
        for k, v in params.items():
            if isinstance(v, str) and '${data.' in v:
                key = v.replace('${data.', '').replace('}', '')
                result[k] = data.get(key, v)
            else:
                result[k] = v
        return result
