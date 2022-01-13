# 10-Fold Cross Validation

{% for fold_name, fold_value in dict_item.items() %}
## {{fold_name}}

avg_dice: {{fold_value.avg_dice}}
    {% for file_name, file_value in fold_value.file_results.items() %}
* {{file_name}}
    * {{file_value}}
    {% endfor %}
{% endfor %}
