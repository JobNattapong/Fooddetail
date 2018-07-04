from selenium import webdriver
from django.test import LiveServerTestCase
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows_text = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows_text])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # ชายหนุ่มได้เจอเว็บแอปใหม่ได้ทำการเข้าไปดูหน้า home page
        self.browser.get(self.live_server_url)
        # และเห็นชื่อ Web app นี่ชื่อว่า Food detail
        self.assertIn('Food Detail', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Food Detail', header_text)
        time.sleep(2)
        # เขาเห็นว่าเว็บแอปนี้สามารถเพื่มรายละเอียดของอาหารได้และลบข้อมูลได้
        # เขาจึงลองใช้เว็บแอปนี้เก็บข้อมูลอาหารที่เขารับประทานเข้าไป
        # เขาเห็นช่องให้กรอก ชื่ออาหาร ปริมาณน้ำตาล ปริมาณโปรตีน
        nameFoof = self.browser.find_element_by_id('name_food')
        nameFoof.send_keys('กระเพาไก่')
        time.sleep(1)

        volumeSugar = self.browser.find_element_by_id('volume_sugar')
        volumeSugar.send_keys(5)
        time.sleep(1)

        volumeProtein = self.browser.find_element_by_id('volume_protein')
        volumeProtein.send_keys(24)
        time.sleep(1)

        # เขาได้ทำการใส่ข้อมูลลงไปและกดเพิ่ม
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(1)
        # เขาจะเห็นว่ารายละเอียดที่กรอกเข้าไปจะไปอยู่ใน list แต่จะขึ้นแค่ชื่ออาหาร
        self.check_for_row_in_list_table('กระเพาไก่ 5 % 24 %')
        # เพิ่มรายละเอียดอาหารอันที่ 2
        nameFoof = self.browser.find_element_by_id('name_food')
        nameFoof.send_keys('ราดหน้า')
        time.sleep(1)

        volumeSugar = self.browser.find_element_by_id('volume_sugar')
        volumeSugar.send_keys(30)
        time.sleep(1)

        volumeProtein = self.browser.find_element_by_id('volume_protein')
        volumeProtein.send_keys(6)
        time.sleep(1)

        # กดเพิ่มรายละเอียดอาหารอันที่ 2
        self.browser.find_element_by_id("id_sub").click()
        time.sleep(1)

        self.check_for_row_in_list_table('กระเพาไก่ 5 % 24 %')
        self.check_for_row_in_list_table('ราดหน้า 30 % 6 %')
        # และเขาสามารถลบข้อมูลที่เพิ่มเข้าไปได้เช่นลบ กระเพาไก่
        delete = self.browser.find_element_by_id('del_input')
        delete.send_keys('กระเพาไก่')
        time.sleep(1)
        # กดลบ
        self.browser.find_element_by_id("id_del").click()
        time.sleep(1)
        # เช็คว่า data1 หายจริงๆ
        table = self.browser.find_element_by_id('id_list_table')
        rows_text = table.find_elements_by_tag_name('tr')
        self.assertNotIn('กระเพาไก่ 5 % 24 %', [row.text for row in rows_text])
        time.sleep(1)
        # ดูข้อมูลที่เหลือ
        self.check_for_row_in_list_table('ราดหน้า 30 % 6 %')
        time.sleep(1)

        # ชายหนุ่มต้องการแก้ไขรายละเอียดอาหารของเขา
        # เขาต้องใส่ ชื่ออาหารที่ต้องการแก้ไข เช่น ราดหน้า
        oldFoof = self.browser.find_element_by_id('old_food')
        oldFoof.send_keys('ราดหน้า')
        time.sleep(1)
        # แก้ไขเป็น ก๋วยเตี๊ยว
        newFoof = self.browser.find_element_by_id('new_food')
        newFoof.send_keys('ก๋วยเตี๋ยว')
        time.sleep(1)
        # ใส่ปริมาณน้ำตาล
        newSugar = self.browser.find_element_by_id('new_sugar')
        newSugar.send_keys(25)
        time.sleep(1)
        # ใส่ปริมาณโปรตีน
        newProtein = self.browser.find_element_by_id('new_protein')
        newProtein.send_keys(10)
        time.sleep(1)
        # กดแก้ไข
        self.browser.find_element_by_id("id_edit").click()
        time.sleep(1)
        # เช็คว่าข้อมูลเปลี่ยนจริงหรือไม่
        self.check_for_row_in_list_table('ก๋วยเตี๋ยว 25 % 10 %')
        time.sleep(2)

        self.fail('Finish the test!')

if __name__ == '__main__': #
    unittest.main(warnings='ignore')
