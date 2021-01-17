Blockly.Python['max90614_object_temp'] = function (block) {
  Blockly.Python.definitions_['import_MLX90614'] = 'import MLX90614';

  var code = 'MLX90614.readObjectTempC()';
  return [code, Blockly.Python.ORDER_NONE];
};

Blockly.Python['max90614_ambient_temp'] = function (block) {
  Blockly.Python.definitions_['import_MLX90614'] = 'import MLX90614';

  var code = 'MLX90614.readAmbientTempC()';
  return [code, Blockly.Python.ORDER_NONE];
};
