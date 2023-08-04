<!DOCTYPE html>
<html>
<head>
    <title>Liste des couleurs</title>
</head>
<body>


    <h1>Liste des couleurs</h1>
    <ul>
        {% for color in colors %}
        <li style="background-color: {{ color.hex_code }};">{{ color.name }} ({{ color.hex_code }})</li>
        {% endfor %}
        {% for voiture in voitures %}
        <li>{{ voiture.nom }} {{ voiture.annee_fabrication }} {{ voiture.marque.nom }}</li>
        {% endfor %}
    </ul>
      
    <a href="{% url 'color_create' %}">Ajouter une couleur</a>
<form method="post">
  {% csrf_token %}
  <div class="form-group">
    <label for="{{ form.color.id_for_label }}">Sélectionnez une couleur :    {{ form.color }}</label>
 
  </div>
  <button type="submit" class="btn btn-primary">Envoyer</button>
</form>

</body>
</html>