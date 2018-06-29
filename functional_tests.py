from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # ชายหนุ่มได้เจอเว็บแอปใหม่ได้ทำการเข้าไปดูหน้า home page
        self.browser.get('http://localhost:8000')
        # และเห็นชื่อ Web app นี่ชื่อว่า Food detail
        self.assertIn('Food Detail', self.browser.title)
        # เขาเห็นว่าเว็บแอปนี้สามารถเพื่มรายละเอียดของอาหารได้และลบข้อมูลได้
        # เขาจึงลองใช้เว็บแอปนี้เก็บข้อมูลอาหารที่เขารับประทานเข้าไป
        # เขาเห็นช่องให้กรอก ชื่ออาหาร ประมาณน้ำตาล ประมาณแป้ง ประมาณไขมัน ประมาณโปรตีน
        # เขาได้ทำการใส่ข้อมูลลงไปและกดเพิ่ม
        # เขาจะเห็นว่ารายละเอียดที่กรอกเข้าไปจะไปอยู่ใน list แต่จะขึ้นแค่ชื่ออาหาร
        # และเขาสามารถคลิกเข้าไปดูรายละเอียดชื่ออาหารนั้นได้
        # และเขาสามารถลบข้อมูลที่เพิ่มเข้าไปได้

        self.fail('Finish the test!')

if __name__ == '__main__': #
    unittest.main(warnings='ignore')
