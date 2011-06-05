#!/usr/bin/env python2
# vim:fileencoding=utf-8

# 时区
timezoneoffset = 8
# 默认的命令前缀
default_prefix = '-'
# 除了 Unicode 分类为“字母”的字符外，昵称里还允许哪些字符。注意即使指定空白
# 符昵称中也不能包含之
allowedSymbolInNick = u'+-_@.™'
# 是否允许多次更改昵称
nick_can_change = True
# 单位是字节。一个汉字为 3 字节
nick_maxlen = 16
# Gtalk 官方中文版使用非加密的协议。检测到 Gtalk 官方中文版用户时要不要提示之。
warnGtalk105 = True
# root 用户，请指定群主的 JID。
root = 'lilydjwg@gmail.com'

# 离开时某些客户端自动发送的消息（全文）
blocked_away_messages = (
  "I'm currently away and will reply as soon as I return to eBuddy on my iPod touch",
)
