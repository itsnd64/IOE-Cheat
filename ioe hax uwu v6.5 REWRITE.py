print("Hiện hỗ trợ bài:Hành tinh tím,Sắp xếp,Heo hồng,True/False,Điền từ")
import mainlib
mainlib.init()

if mainlib.questypetest == 10:mainlib.baibth()
if mainlib.questypetest == 5 or (mainlib.questypetest == 3 and mainlib.quespointtest == 10):mainlib.baisapxep()
if mainlib.questypetest == 1 and mainlib.subjecttypetest == False:mainlib.baitf()
if mainlib.subjecttypetest == True and mainlib.quespointtest == 25:mainlib.baitf4cau()
if "*" in mainlib.quescontenttest:mainlib.baidientu()
if mainlib.quespointtest == 100:mainlib.baiconlon()