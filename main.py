from PIL import Image

# foydalanuvchidan rasm fayl nomini so'raymiz
file_name = input("Iltimos, rasm fayl nomini kiriting: ")

# rasm faylini o'qib olamiz
try:
    img = Image.open(file_name)
except:
    print("Rasm faylini ochib bo'lmadi!")
    exit()

# rasmning o'lchamini o'zgartirish uchun yangi height va width qiymatlarni foydalanuvchidan so'raymiz
new_width = int(input("Yangi rasmning enini kiriting (px): "))
new_height = int(input("Yangi rasmning bo'lini kiriting (px): "))

# rasmni o'lchamlarini o'zgartiramiz
img = img.resize((new_width, new_height))

# yangi faylnomni so'raymiz va rasmni yangi faylga yozamiz
new_file_name = input("Yangi fayl nomini kiriting: ")
img.save(new_file_name)

print("Rasm o'lchami o'zgartirildi va yangi fayl saqlandi!")
