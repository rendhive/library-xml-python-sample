import xml.etree.ElementTree as ET

xml_data = '''<config>
    <setting name="theme">dark</setting>
    <setting name="language">en</setting>
</config>'''

root = ET.fromstring(xml_data)
theme = root.find('./setting[@name="theme"]').text
print("Current theme:", theme)
# Fungsi: Menggunakan XML untuk menyimpan konfigurasi aplikasi.
# Kondisi: Ketika Anda ingin menyimpan pengaturan dan membacanya dengan mudah.