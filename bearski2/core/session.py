"""测试会话管理"""
from typing import Any, Dict, Optional

class TestSession:
    """测试会话 - 管理所有驱动和共享数据"""
    
    def __init__(self):
        self.context: Dict[str, Any] = {}
        self.db_connection = None
        self.rest_session = None
        self.ui_browser = None
    
    def set(self, key: str, value: Any):
        """保存数据到上下文"""
        self.context[key] = value
    
    def get(self, key: str, default=None) -> Any:
        """从上下文获取数据"""
        return self.context.get(key, default)
    
    def cleanup(self):
        """清理所有连接"""
        if self.db_connection:
            self.db_connection.close()
        if self.rest_session:
            self.rest_session.close()
        if self.ui_browser:
            self.ui_browser.close()
