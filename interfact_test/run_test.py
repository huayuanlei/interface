import unittest
import HTMLReport

# 运行这个文件，就能跑起来了 
test_dir = "testcase/message"
suits = unittest.defaultTestLoader.discover(test_dir, pattern="*.py")

if __name__ == "__main__":
    runner = HTMLReport.TestRunner()
    runner.run(suits)
