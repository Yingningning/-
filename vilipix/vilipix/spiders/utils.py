import re
def decode_specific_parts(content):
    # 使用正则表达式匹配 \uxxxx 形式的字符串
    pattern = re.compile(r'(\\u[a-zA-Z0-9]{4})')
    
    # 对匹配到的每一部分进行解码
    def decode_match(match):
        return match.group().encode('utf-8').decode('unicode_escape')
    
    # 替换原字符串中的内容
    return pattern.sub(decode_match, content)
