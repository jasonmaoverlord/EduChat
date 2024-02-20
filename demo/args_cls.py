#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Project ：EduChat 
# @File    ：args_cls.py
# @Author  ：JasonMa
# @Date    ：2024/2/16 10:13 PM

class ArgsClass:

    def __init__(self, model_path, max_new_tokens, top_k, do_sample, per_digit_tokens):
        self.model_path = model_path
        self.max_new_tokens = max_new_tokens
        self.top_k = top_k
        self.do_sample = do_sample
        self.per_digit_tokens = per_digit_tokens
