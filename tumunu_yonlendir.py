import os
import re

# İşlem yapılacak klasör
posts_dir = '_posts'

islenen_dosya_sayisi = 0
atlanan_dosya_sayisi = 0

for filename in os.listdir(posts_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Dosyada zaten redirect_from etiketi varsa (örneğin test ettiğimiz algoritma.md) atla
        if 'redirect_from:' in content:
            atlanan_dosya_sayisi += 1
            continue
            
        # Dosya adından URL uzantısını (slug) çıkarma
        match = re.search(r'(?:\d{4}-\d{2}-\d{2}-)?(.+)\.md', filename)
        
        if match:
            slug = match.group(1)
            old_url = f"/posts/{slug}/"
            
            # YAML Front matter bloğunu bulup araya kodu ekleme
            parts = content.split('---', 2)
            
            if len(parts) >= 3:
                redirect_block = f"redirect_from:\n  - {old_url}\n"
                new_content = f"---{parts[1]}{redirect_block}---{parts[2]}"
                
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                print(f"Eklendi: {filename} -> {old_url}")
                islenen_dosya_sayisi += 1
            else:
                print(f"Uyarı: {filename} dosyasında geçerli bir front matter bulunamadı.")

print("-" * 30)
print(f"İşlem Tamamlandı! Toplam güncellenen dosya: {islenen_dosya_sayisi}, Zaten hazır olan/atlanan: {atlanan_dosya_sayisi}")