# file_integrity_log

This Repository for NEIS0736

## Inspiration
Code มาจากตัวอย่างของเพื่อนในห้องเรียนวิชา  NEIS0736 Software Security ในหัวข้อ File Integrity Monitoring (FIM) ซึ่งเป็นตัวอย่างการเขียน FIM อย่างง่ายในการตรวจสอบการเปลี่ยนแปลงข้อมูลของ file ที่เราสนใจ ซึ่งสามารถเพิ่มความมั่นคงปลอดภัยได้ 
จาก ตัวอย่าง code จะสามารถแจ้ง alert การเปลี่ยนแปลงผ่านทาง console ได้ ทางทีมจึงนำ code ดังกล่าวมาต่อยอดโดยทำการเพิ่มฟังก์ชั่นในการทำ log file เพื่อเก็บข้อมูลการเปลี่ยนแปลงไฟล์และเวลาที่ถูกเปลี่ยนแปลงไว้ เพื่อให้สามารถทำการตรวจสอบ log ย้อนหลังได้

```python
# improvise log function
def fim_log(msg):
    f = open('fimlog/fimlog.txt', 'a')
    f.write(msg + '\n')
    f.close()
```
## Team
Vatcharin Kongsakul 

Ekawut  Chairat
