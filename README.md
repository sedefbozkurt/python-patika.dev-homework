# Python Patika.dev Ödevi

Bu repo iki işlevi içerir:

1. **flatten_list**: İç içe geçmiş listeyi düzleştirir.
2. **reverse_nested_list**: İç içe geçmiş bir listeyi ve onun alt listelerini tersine çevirir.

**flatten_list:**

```python
input_list = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_list = flatten_list(input_list)
print(output_list)  # Çıktı: [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
```

**reverse_nested_list:**

```python
input_list = [[1, 2], [3, 4], [5, 6, 7]]
output_list = reverse_nested_list(input_list)
print(output_list)  # Çıktı: [[7, 6, 5], [4, 3], [2, 1]]
```
