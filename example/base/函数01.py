def test():
    print("这是测试")

# 层叠打印日志 mp_bar_code_print_log
def testFor():
    nums = ''
    idx=0;
    for i in range(849178532, 849178981):
        pre = "( '13', '2022-01-24 09:00:00', NULL, '2022-01-24 09:00:00', NULL, "
        code = "'63XX51220122100" + str(i)+"',"
        post = "'2', '2', '-', '-', '9-2201016', '2'),"
        nums = nums+(pre+code+post)
        idx +=1
    print(idx)
    print(nums)

# mf_production_line产线刷入表
# INSERT INTO mf_production_line
# (CREATED_BY,CREATED_TIME,IS_VALID,IS_DELETED,PLAN_ID,BILL_NO,ORDER_NO,BAR_CODE_ID,
# BAR_CODE,
# SITE_ID,SITE_CODE,SITE_NAME,JUDGEMENT,SOURCE,BELTLINE,GROUP_STAFFS)
# VALUES
# (162,'2022-01-24 09:00:00.0','Y','N',166134996231320,'SRP-EMN-IN-220001','9-2201016',null,
# '63XX51220122100849178532',4,'01','层叠','0','5','013','自动刷入');
def testFor2():
    nums = ''
    for i in range(849178532, 849178981):
       # pre = "(162,'2022-01-24 09:00:00.0','Y','N',166134996231320,'SRP-EMN-IN-220001','9-2201016',null,"
        code = "'63XX51220122100" + str(i)+"',"
        #post = "4,'01','层叠','0','5','013','自动刷入'),"
        #nums = nums+(pre+code+post)
        nums = nums+(code)
    print(nums)



if __name__ == '__main__':
    test()
