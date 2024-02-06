# Hausdorff distances

dict_item['existing_folds'] {{ dict_item['existing_folds'] }}
{% set labels = dict_item['labels'] %}
dict_item['labels'] {{ labels }}
{% set path_segs = dict_item['paths_segs'] %}
dict_item['paths_segs'] {{ path_segs }}
dict_item['hausdorff_data'] {{ dict_item['hausdorff_data'] }}

{% set i = namespace(v=0) %} 
{% for x in dict_item['hausdorff_data'] %}
## {{ path_segs[i.v] }}
    {% set j = namespace(value=0) %}
    {% for y in x %}
        {{ labels[j.value] }} | {{ y }}
        {% set j.value = j.value + 1 %}
    {% endfor %}
    {% set i.v = i.v + 1 %}
{% endfor %}
