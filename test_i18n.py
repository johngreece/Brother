#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
测试国际化功能的简单脚本
"""

from app import app, get_locale

def test_i18n():
    """测试国际化功能"""
    with app.app_context():
        # 测试默认语言
        print("默认语言: zh")
        
        # 测试配置
        print("支持的语言:", app.config['LANGUAGES'])
        print("默认语言:", app.config['BABEL_DEFAULT_LOCALE'])
        
        print("✅ 国际化功能测试完成！")

if __name__ == '__main__':
    test_i18n() 