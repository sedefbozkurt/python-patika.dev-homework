# Bu fonksiyon, bir liste içindeki tüm iç içe geçmiş liste elemanlarını tek bir düz liste haline getirir
def flatten_list(nested_list):
  flat_list = []

  def flatten(item):
    if isinstance(item, list): # elemanın liste olup olmadığını kontrol eder
      for sub_item in item:
        flatten(sub_item)
    else:
      flat_list.append(item)
  
  flatten(nested_list)
  return flat_list

# Bu fonksiyon, bir liste içindeki elemanları tersine döndürür 
# eğer eleman yine bir listeyse onun elemanlarını da tersine çevirir
def reverse_nested_list(nested_list):
  if isinstance(nested_list, list):
    return [reverse_nested_list(item) for item in reversed(nested_list)]
  return nested_list