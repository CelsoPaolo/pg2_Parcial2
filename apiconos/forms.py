from django import forms
from apiconos.models import PedidoCono
# Importamos el serializador para usar la misma lista de ingredientes permitidos
from apiconos.serializers import PedidoConoSerializer


class PedidoConoAdminForm(forms.ModelForm):
    """
    Formulario personalizado para el modelo PedidoCono en el panel de administración de Django.
    Incluye validación para el campo 'ingredientes'.
    """
    class Meta:
        model = PedidoCono
        fields = '__all__' # Incluye todos los campos del modelo

    def clean_ingredientes(self):
        """
        Método de limpieza personalizado para el campo 'ingredientes'.
        Valida que cada ingrediente esté en la lista permitida.
        """
        ingredientes = self.cleaned_data.get('ingredientes')
        
        # Asegurarse de que ingredientes es una lista, incluso si es None o si el JSONField no lo parseó como lista
        if not isinstance(ingredientes, list):
            # Si no es una lista después de la limpieza del JSONField, es un error de formato grave.
            raise forms.ValidationError("El formato de los ingredientes debe ser una lista JSON válida (ej. [\"queso_extra\"]).")

        # Obtener la lista de ingredientes válidos desde el serializador para consistencia
        ingredientes_permitidos = PedidoConoSerializer.INGREDIENTES_PERMITIDOS

        for ingrediente in ingredientes:
            if not isinstance(ingrediente, str):
                raise forms.ValidationError("Cada elemento en la lista de ingredientes debe ser un texto.")
            if ingrediente not in ingredientes_permitidos:
                # Mensaje de error más conciso para el administrador
                raise forms.ValidationError(f"El ingrediente '{ingrediente}' no está disponible.") 
        return ingredientes