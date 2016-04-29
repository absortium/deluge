__author__ = 'andrew.shvv@gmail.com'

from rest_framework import serializers

from ethclient.model.models import Account, Address


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `exclude_fields` argument that
    controls which fields should be excluded from serialization.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        exclude_fields = kwargs.pop('exclude_fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if exclude_fields:
            # Drop any fields that are not specified in the `fields` argument.
            disallowed = set(exclude_fields)

            for field_name in disallowed:
                self.fields.pop(field_name)


class AccountSerializer(serializers.ModelSerializer):
    amount = serializers.ReadOnlyField()

    class Meta:
        model = Account
        fields = ('pk', 'amount')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._object = None

    def object(self, **kwargs):
        if not self._object:
            validated_data = dict(
                list(self.validated_data.items()) +
                list(kwargs.items())
            )

            self._object = Account(**validated_data)
        return self._object


class AddressSerializer(serializers.ModelSerializer):
    amount = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()

    class Meta:
        model = Address
        fields = ('pk', 'amount', 'address', 'created')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._object = None

    def object(self, **kwargs):
        if not self._object:
            validated_data = dict(
                list(self.validated_data.items()) +
                list(kwargs.items())
            )

            self._object = Account(**validated_data)
        return self._object
