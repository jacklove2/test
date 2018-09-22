from HTMLTestRunner import HTMLTestRunner
import unittest,time,os
current_path=os.path.dirname(os.path.realpath(__file__))
test_case=os.path.join(current_path,'test_case')
test_report=os.path.join(current_path,'report')
test_list=unittest.defaultTestLoader.discover(test_case,pattern='test*.py')
if __name__ == '__main__':
    now=time.strftime('%Y_%m_%d_%H_%M_%S')
    filename=test_report+'\\'+ now +'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='自动化测试项目',
                          description='ui自动化测试执行情况：')
    runner.run(test_list)
    fp.close()