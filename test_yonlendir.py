import os
import re

# _posts klasörünün yolu
posts_dir = '_posts'
# Test etmek istediğin dosyanın adının bir kısmı veya tamamı
target_keyword = 'algoritma' 

# Klasördeki dosyaları tara
for filename in os.listdir(posts_dir):
    # Sadece hedef kelimeyi içeren ve .md ile biten İLK dosyayı bul
    if target_keyword in filename and filename.endswith('.md'):
        filepath = os.path.join(posts_dir, filename)
        print(f"Test edilecek dosya bulundu: {filename}")
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if 'redirect_from:' in content:
            print("Bu dosyada zaten 'redirect_from' etiketi var. İşlem iptal edildi.")
            break
            
        # Dosya adından URL uzantısını (slug) çıkarma işlemi
        # Başında tarih (YYYY-MM-DD-) varsa yoksayar, sadece asıl adı alır
        match = re.search(r'(?:\d{4}-\d{2}-\d{2}-)?(.+)\.md', filename)
        
        if match:
            slug = match.group(1)
            old_url = f"/posts/{slug}/"
            
            # YAML Front matter bloklarını ayırıp araya kodu enjekte etme
            parts = content.split('---', 2)
            
            if len(parts) >= 3:
                redirect_block = f"redirect_from:\n  - {old_url}\n"
                # Yeni içeriği birleştir
                new_content = f"---{parts[1]}{redirect_block}---{parts[2]}"
                
                # Dosyayı yeni haliyle üzerine yazarak kaydet
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                print(f"Başarılı! YAML bloğuna eklendi:\n  - {old_url}")
            else:
                print("Hata: Dosyada geçerli bir '---' front matter bloğu bulunamadı.")
        
        # Test versiyonu olduğu için ilk bulduğu dosyayı işleyip döngüyü kırar
        break
else:
    print(f"İçinde '{target_keyword}' geçen bir .md dosyası bulunamadı.")