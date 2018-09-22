from HTMLTestRunner import HTMLTestRunner
import unittest,time,os

current_path=os.path.dirname(os.path.realpath(__file__))
test_case1=os.path.join(current_path,'test_case1')
test_report1=os.path.join(current_path,'report1')
test_list=unittest.defaultTestLoader.discover(test_case1,pattern='test*.py')
if __name__ == '__main__':
    now=time.strftime('%Y_%m_%d_%H_%M_%S')
    filename=test_report1+'\\'+ now +'_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='接口自动化测试项目',
                          description='接口自动化测试用例执行情况：')
    runner.run(test_list)
    fp.close()