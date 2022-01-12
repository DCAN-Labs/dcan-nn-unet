# 10-Fold Cross Validation

{% for key, value in dict_item.items() %}
## {{key}}

avg_dice: value.avg_dice
    {% for inner_key, inner_value in value.file_results.items() %}
* {{inner_key}}
    * {{inner_value}}
    {% endfor %}
{% endfor %}
