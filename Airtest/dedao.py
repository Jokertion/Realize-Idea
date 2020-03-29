#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: jokertion
@file: dedao.py
@time: 2020/3/29 15:20
@desc: 
"""

from airtest.core.api import *
import time
auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

words = ['百年孤独', '如何阅读一本书', '少有人走的路', '乌合之众', '追风筝的人', '万历十五年', '红楼梦', '三体', '失控', '白夜行', '不能承受的生命之轻', '社会心理学', '心理学与生活', '小王子', '影响力', '哥德尔、艾舍尔、巴赫', '通往奴役之路', '历史深处的忧虑', '霍乱时期的爱情', '枪炮、病菌与钢铁', '月亮和六便士', '论美国的民主', '送你一颗子弹', '中国历代政治得失', '文学回忆录（全2册）', '围城', '民主的细节', '寻路中国', '人类简史', '艺术的故事', '解忧杂货店', '看不见的城市', '天才在左 疯子在右', '高效能人士的七个习惯（精华版）', '设计中的设计', '目送', '看见', '江城', '娱乐至死', '情人', '把时间当作朋友', '社会契约论', '我们仨', '社会性动物', '理想国', '自控力', '思考，快与慢', '国史大纲（上下）', '写给大家看的设计书（第3版）', '狂热分子', '遇见未知的自己', '苏菲的世界', '天朝的崩溃', '这些人，那些事', '嫌疑人X的献身', '牧羊少年奇幻之旅', '浪潮之巅', '挪威的森林', '菊与刀', '一九八四', '史记（全十册）', '查令十字街84号', '从一到无穷大', '爱的艺术', '决策与判断', '黑客与画家', '学会提问', '心是孤独的猎手', '点石成金', '自私的基因', '孤独六讲', '最好的告别', '卡拉马佐夫兄弟', '窗边的小豆豆', '刀锋', '三体Ⅱ', '故事', '亲爱的安德烈', '三体Ⅲ', '卓有成效的管理者', '沟通的艺术（插图修订第14版）', '《华尔街日报', '当我谈跑步时我谈些什么', '活着', '中国大历史', '西方哲学史（上卷）', '夹边沟记事', '无声告白', '定位', '何以笙箫默', '总统是靠不住的', '设计心理学', '万物静默如谜', '平凡的世界（全三部）', '我也有一个梦想', '最初的爱情 最后的仪式', '规训与惩罚', '认识电影', '沉默的大多数', '带一本书去巴黎']

# 启动app
# poco(text="得到").click()

for word in words:
    # 点击搜索框
    poco("com.luojilab.player:id/et_search").click()

    # 在搜索框输入内容
    text(word, search=True)
    time.sleep(2)
    poco('com.luojilab.player:id/btn_search_cancel').click()
    
