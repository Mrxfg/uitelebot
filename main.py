from telebot import TeleBot, types
bot = TeleBot(token="5505404288:AAHL6Wzu8xod15c3YwGn0oOP8FBNE0dw7MQ")

channel = "@LAMPA_VPN"
checkbtns = types.InlineKeyboardMarkup(row_width=2)
checkbtns.add(
    types.InlineKeyboardButton(text="1-Kanal", url="https://t.me/LAMPA_VPN"),
    types.InlineKeyboardButton(text="2-Kanal", url="https://t.me/hamster_Kombat_bot/start?startapp=kentId6475478048"),
    types.InlineKeyboardButton(text="KANALA AGZA BOLDUM☑️",callback_data="checksub")
)


@bot.message_handler(commands=["start"])
def start(msg: types.Message):
    checkuser = bot.get_chat_member(channel, msg.from_user.id).status
    if checkuser == 'member' or checkuser == 'admin' or checkuser == 'creator':
        bot.send_message(msg.from_user.id, "darktunnel://eyJ0eXBlIjoiU1NIIiwibmFtZSI6IkRPU0xBUiBTSVogVUNJTiBZQVJZUCBEVVJBTiBWUE7wn5qAIiwic3NoVHVubmVsQ29uZmlnIjp7ImluamVjdENvbmZpZyI6eyJlbmFibGVkIjp0cnVlLCJtb2RlIjoiUFJPWFkifX0sImVuY3J5cHRlZExvY2tlZENvbmZpZyI6IkZmTGpHcE1QbjkzMjJ2VDE2MEZwVGJOcTV4Sm1jWkN1R2d4RElxbHJpOVc4SE5XaTNkQzFDWmRJTXgxWjFiQ20zeFhSTHlGTTJFY20xY3RBTXFaaDEtSTRfbjZkU29LMTQtZkRDMmhzekFBTUtoU01BdWNCUWdqWFhUNlRuNzd0YnlCX0pfcnllQTFpa29yMWZ5TVcwcXI0NE9IQkNHLXhlbkFrUWpHcnE4S3F2T2lWYlo5WmtNWVAzVTRWUktWaDFtV1FvSDdpQXBNTXl0RmRKclFJMjNGSHFTR2JCQnJiT3VYaWEzMEVWRDRxZlRmUFczOUw3ZEktSjhvdWJBY3FKWXllcHhsTGlaYnFReEhOcUJXZExvcU1tZzlwSzRHTWliTk4zRkFXV0ZmWWRNTFN2SjlxNU5melR1ZDJiOTA4WU1aeTc5NzA4V0h5bVpyVXg5UUlpSjhLWUc1ejdmeVJCUmNBMjhoaUtETWlRZG90d0RiZkE1dGdoZ1hOZ3VGNFpDSmhfdXFJbk1VT09fZnY3RzBXcUVpMXFGZmxKMGZLOHFmSTFlM0p6dXdER0xySHFyU0REN0xfbGZoeTlHZmg2VU8tUWY2RGIzNmJOSEstZ2dqSzk1bnVxSklSTG1HRUxPV25SUGxMazJxRmlqRFVSNlpTZlF4eEgtdEF0VmQzYnN4alVaNHd6ZmFzSDhneDRPRDA0dUNyeFotOVFyUHhIWHdVMm5Sdk1BcTZFal9lclRfWHllX2R0TWdPZWRnX0puUjQ0elJjeEFQaGRrcVpEWHpITE9hWUtNdUFpSUNzcmd1OW5SSi16Ym45WkVFcFpUTTVXcXpvcUk2VFZKSFV2S3UxNTRVOGRhSUtHS3lmSzZOcWVTWHQ5VVNWWXBLRnlSckVnVU5ud2cwT09CS3lpWGpMdVZ2d181NFlhQWdia2F2Ym9nR2JZMkdDaXktcmpvZkZTSUQyNk1ocXZCc2ZOSlEwSVZrQi1sdTk0VnJlZE51S1E5VFp1WVVXSFBQRjAxVWlRb1Z1MDZqcTd2RWpvaWprSkRaOFRJbkc1MExHM0M5NlQwc2JaRk9lLThqeXpfNF9Rc1UxbWN6eEV0NDlZOEZGeC1NX2MzajF3OFVFbHg3bC0zbTByTmlEN2JMSnBQSlpGV29JdGh5a2haV0M5SVBLSG9QYXlZaWVmWWYyblRRbnZ5TWw0R0ZSWW1TTm1OM1ljWllxbWN3VGpBWWJkYmxwYTdPX18ycWVic3N2dEZjTHJ6MkIzakJYSUg5S0VIa053bExfQ0ppNldjSVRHbmVfZkNJcTVQU3dBbkhHaFBSd1NRQ1Jyb21DR3lnaGR6SVFlNG41SWVMMEZ0SThDU0FrU0V1UlNka19EbmV6emdBSDlPY0N4aHhyZHZtVjhDTzJEUkNudDZBb1c0ZmREYmpRZFFxLXZQNmJKczVxRHZZY1NNLUlIRGZFZGIxSmt4YjBkWlRaRGlzMS1OelVlaDRZNGxmdTJQZHMwWjUyUGphY3BuYmMtUlhFSV9Mb09aZGNjZ2dRV1NoMXZSem5BTnBSUUE1NGI1cHh6bVp3WnpLRUpTdm1mRy1PVWoyUmhQNVFLRkV4UFdRUEZYeGVoOUhJX3NZQkp0RjV2ZUFMQkM2WG9rRzV5Zm9ObUZKc09nTzY1X1JWbEtNanhUaXhqUU1tS1owdVpHa3NPTWt0SHhxeVUtUjJzZnZmS09oQnJUckQtQy1JaWJrYmlsZm5WUFhpakhtc0swazV3eVdQWTNJTTFsUUt6US01X1JwMzB3SENtcTNLZThyRzdWbDZYOWQxaHhEQzM1ZUwyLVlSb25rR1dLbnlhV0s3Y3g1M1k1cTlxa1RYM0xnUDFNS0hSUjJhS1hMay13TVdFRGFzd0c2TlJlMEFCb3puc25tME1BZVYzZkpJaDRlbF9oSlhIS0xWTzY5T3dfSXNBbGNnUkt6ZUpfcy1WVWlIQzNYWG12RVU2Nk91QXFKb1A1MFAtS1RjZjVBX1pDUXQ5cTBSZ3JEd3hrZDQ4bkVXa3dDUDhPS2FBRHpKWElTNnBuLXhKV0NVZUN1cUl3U0xMem5CRjI0cENPVWJ2bDU5Wi1DQ0tENGxXc0JQbVZ2ZXBQd3lkTkFxeUkzVjg2bko0ZUxVT3NaV3RVam9kOWltVlVySWtnT3hoYWZ2RmtlMUR4Q0d5R01XaGs3OWNKanZ0ZS1YYXhESGlQc0l3aDRXUmJ4clFNUDEtT19KUFBtRVc2aWtIQVlDcXg0RWZ3bUxoaGJTSHhfcm9ONFBMd1VNLVpVemxSWnpVZnA2TThoRmdhX2lhNE83cG1lcjh4YzBuSk9nNXl0WlVGN2hWRU5wOVJlbnFCeW1NMmpQc05XMFA2dHRnQXNsRldNX2R6d2E4NGRHNGRhQUNUVWhlODFkbF9XZFdFdzVkS3Y1SGc5UmZzQ0JDeGJjVDZQejJ6S3JDU1B0TWtycjdfcDM0TWZfdWlkaUpYeG04VkNudDhCbmJyVlhrMkNucW1HRnE0VE45Y0x6Y2lILTdPSHBWQkpLY0xuX0Z6ZXRJQzU3eG5FQ0FtUzgwUGZsMHJIWmZJTG5UaGpzMnBRdzMtTHM0REQteGd5VTREV3BNRzZSOWlMZzZIV0xtWUk2eG9oY0JCWlhmM2oyVFBKSzUwQUk0Q1QxRk5GcnBkRW0tTDVWWXRqczVKOXI0UTN2WWxQeF93aEZUWWlqb3ZzWUF3UWkwbl9kazNna3VheG9BUEh6STJhQ0JIcGhYT1lSUkxac3hCTnE4Rm9BTTJ0NHlTRnV3N2lXSXRIMFE1ZWtfbElqcnRCTHB0MFhiUGRjc1NQWHJBbU5yVC1zNFA2elFTZmI3ZnpaZWhabHJHYTEwOGhnWDI3YkhySzBFT0lBYzZpODFhUU0xcWZQRmV2ZFZxcXJ3Q09Vbkw4aS1NTjJXQmtpNGJsdmExcTdFcVR2VHlKR3BMU1BuTDRaWmZhRWg4UHV5VnR1RF9qa2I5ZHNuQjd3LXJjTlE0SkgxUXRPTzNXS0tiTDJzbVN1RGJWZDdUM0Zpd1c4MWJ2UUotZE53djBHQ25ZQUxHU3U5c0N6V0NmbUx0eVRYbkJWWFdkelZJcFgifQ==")
    else:
        bot.send_message(msg.from_user.id,f'Salam {msg.from_user.first_name} Asakdaky kanallara agza bolun!!', reply_markup=checkbtns)

@bot.callback_query_handler(func=lambda x: x.data)
def query(msg: types.CallbackQuery):
    match msg.data:
        case "checksub":
             checkuser = bot.get_chat_member(channel, msg.from_user.id).status
             if checkuser == 'member' or checkuser == 'admin' or checkuser == 'creator':
                bot.send_message(msg.from_user.id, "darktunnel://eyJ0eXBlIjoiU1NIIiwibmFtZSI6IkRPU0xBUiBTSVogVUNJTiBZQVJZUCBEVVJBTiBWUE7wn5qAIiwic3NoVHVubmVsQ29uZmlnIjp7ImluamVjdENvbmZpZyI6eyJlbmFibGVkIjp0cnVlLCJtb2RlIjoiUFJPWFkifX0sImVuY3J5cHRlZExvY2tlZENvbmZpZyI6IkZmTGpHcE1QbjkzMjJ2VDE2MEZwVGJOcTV4Sm1jWkN1R2d4RElxbHJpOVc4SE5XaTNkQzFDWmRJTXgxWjFiQ20zeFhSTHlGTTJFY20xY3RBTXFaaDEtSTRfbjZkU29LMTQtZkRDMmhzekFBTUtoU01BdWNCUWdqWFhUNlRuNzd0YnlCX0pfcnllQTFpa29yMWZ5TVcwcXI0NE9IQkNHLXhlbkFrUWpHcnE4S3F2T2lWYlo5WmtNWVAzVTRWUktWaDFtV1FvSDdpQXBNTXl0RmRKclFJMjNGSHFTR2JCQnJiT3VYaWEzMEVWRDRxZlRmUFczOUw3ZEktSjhvdWJBY3FKWXllcHhsTGlaYnFReEhOcUJXZExvcU1tZzlwSzRHTWliTk4zRkFXV0ZmWWRNTFN2SjlxNU5melR1ZDJiOTA4WU1aeTc5NzA4V0h5bVpyVXg5UUlpSjhLWUc1ejdmeVJCUmNBMjhoaUtETWlRZG90d0RiZkE1dGdoZ1hOZ3VGNFpDSmhfdXFJbk1VT09fZnY3RzBXcUVpMXFGZmxKMGZLOHFmSTFlM0p6dXdER0xySHFyU0REN0xfbGZoeTlHZmg2VU8tUWY2RGIzNmJOSEstZ2dqSzk1bnVxSklSTG1HRUxPV25SUGxMazJxRmlqRFVSNlpTZlF4eEgtdEF0VmQzYnN4alVaNHd6ZmFzSDhneDRPRDA0dUNyeFotOVFyUHhIWHdVMm5Sdk1BcTZFal9lclRfWHllX2R0TWdPZWRnX0puUjQ0elJjeEFQaGRrcVpEWHpITE9hWUtNdUFpSUNzcmd1OW5SSi16Ym45WkVFcFpUTTVXcXpvcUk2VFZKSFV2S3UxNTRVOGRhSUtHS3lmSzZOcWVTWHQ5VVNWWXBLRnlSckVnVU5ud2cwT09CS3lpWGpMdVZ2d181NFlhQWdia2F2Ym9nR2JZMkdDaXktcmpvZkZTSUQyNk1ocXZCc2ZOSlEwSVZrQi1sdTk0VnJlZE51S1E5VFp1WVVXSFBQRjAxVWlRb1Z1MDZqcTd2RWpvaWprSkRaOFRJbkc1MExHM0M5NlQwc2JaRk9lLThqeXpfNF9Rc1UxbWN6eEV0NDlZOEZGeC1NX2MzajF3OFVFbHg3bC0zbTByTmlEN2JMSnBQSlpGV29JdGh5a2haV0M5SVBLSG9QYXlZaWVmWWYyblRRbnZ5TWw0R0ZSWW1TTm1OM1ljWllxbWN3VGpBWWJkYmxwYTdPX18ycWVic3N2dEZjTHJ6MkIzakJYSUg5S0VIa053bExfQ0ppNldjSVRHbmVfZkNJcTVQU3dBbkhHaFBSd1NRQ1Jyb21DR3lnaGR6SVFlNG41SWVMMEZ0SThDU0FrU0V1UlNka19EbmV6emdBSDlPY0N4aHhyZHZtVjhDTzJEUkNudDZBb1c0ZmREYmpRZFFxLXZQNmJKczVxRHZZY1NNLUlIRGZFZGIxSmt4YjBkWlRaRGlzMS1OelVlaDRZNGxmdTJQZHMwWjUyUGphY3BuYmMtUlhFSV9Mb09aZGNjZ2dRV1NoMXZSem5BTnBSUUE1NGI1cHh6bVp3WnpLRUpTdm1mRy1PVWoyUmhQNVFLRkV4UFdRUEZYeGVoOUhJX3NZQkp0RjV2ZUFMQkM2WG9rRzV5Zm9ObUZKc09nTzY1X1JWbEtNanhUaXhqUU1tS1owdVpHa3NPTWt0SHhxeVUtUjJzZnZmS09oQnJUckQtQy1JaWJrYmlsZm5WUFhpakhtc0swazV3eVdQWTNJTTFsUUt6US01X1JwMzB3SENtcTNLZThyRzdWbDZYOWQxaHhEQzM1ZUwyLVlSb25rR1dLbnlhV0s3Y3g1M1k1cTlxa1RYM0xnUDFNS0hSUjJhS1hMay13TVdFRGFzd0c2TlJlMEFCb3puc25tME1BZVYzZkpJaDRlbF9oSlhIS0xWTzY5T3dfSXNBbGNnUkt6ZUpfcy1WVWlIQzNYWG12RVU2Nk91QXFKb1A1MFAtS1RjZjVBX1pDUXQ5cTBSZ3JEd3hrZDQ4bkVXa3dDUDhPS2FBRHpKWElTNnBuLXhKV0NVZUN1cUl3U0xMem5CRjI0cENPVWJ2bDU5Wi1DQ0tENGxXc0JQbVZ2ZXBQd3lkTkFxeUkzVjg2bko0ZUxVT3NaV3RVam9kOWltVlVySWtnT3hoYWZ2RmtlMUR4Q0d5R01XaGs3OWNKanZ0ZS1YYXhESGlQc0l3aDRXUmJ4clFNUDEtT19KUFBtRVc2aWtIQVlDcXg0RWZ3bUxoaGJTSHhfcm9ONFBMd1VNLVpVemxSWnpVZnA2TThoRmdhX2lhNE83cG1lcjh4YzBuSk9nNXl0WlVGN2hWRU5wOVJlbnFCeW1NMmpQc05XMFA2dHRnQXNsRldNX2R6d2E4NGRHNGRhQUNUVWhlODFkbF9XZFdFdzVkS3Y1SGc5UmZzQ0JDeGJjVDZQejJ6S3JDU1B0TWtycjdfcDM0TWZfdWlkaUpYeG04VkNudDhCbmJyVlhrMkNucW1HRnE0VE45Y0x6Y2lILTdPSHBWQkpLY0xuX0Z6ZXRJQzU3eG5FQ0FtUzgwUGZsMHJIWmZJTG5UaGpzMnBRdzMtTHM0REQteGd5VTREV3BNRzZSOWlMZzZIV0xtWUk2eG9oY0JCWlhmM2oyVFBKSzUwQUk0Q1QxRk5GcnBkRW0tTDVWWXRqczVKOXI0UTN2WWxQeF93aEZUWWlqb3ZzWUF3UWkwbl9kazNna3VheG9BUEh6STJhQ0JIcGhYT1lSUkxac3hCTnE4Rm9BTTJ0NHlTRnV3N2lXSXRIMFE1ZWtfbElqcnRCTHB0MFhiUGRjc1NQWHJBbU5yVC1zNFA2elFTZmI3ZnpaZWhabHJHYTEwOGhnWDI3YkhySzBFT0lBYzZpODFhUU0xcWZQRmV2ZFZxcXJ3Q09Vbkw4aS1NTjJXQmtpNGJsdmExcTdFcVR2VHlKR3BMU1BuTDRaWmZhRWg4UHV5VnR1RF9qa2I5ZHNuQjd3LXJjTlE0SkgxUXRPTzNXS0tiTDJzbVN1RGJWZDdUM0Zpd1c4MWJ2UUotZE53djBHQ25ZQUxHU3U5c0N6V0NmbUx0eVRYbkJWWFdkelZJcFgifQ==")
             else:
                bot.send_message(msg.from_user.id, "Hemmesine agza bolmadynyz!!", reply_markup=checkbtns)

bot.polling()
