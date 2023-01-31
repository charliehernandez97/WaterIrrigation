PROGRAM WaterIrrigation
  VAR
    VALVE AT %IX0.0 : BOOL;
    PUMP AT %QX0.0 : BOOL;
  END_VAR
  VAR
    TP0 : TP;
    pulse : TIME := T#10000ms;
  END_VAR

  TP0(IN := VALVE, PT := pulse);
  PUMP := TP0.Q;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : WaterIrrigation;
  END_RESOURCE
END_CONFIGURATION
