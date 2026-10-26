def diagnose_measurement(measurement):       
    """Return the diagnostic status and message for one measurement."""
    
    if "value" not in measurement or "received" not in measurement:
        return '| Status: INVALID DATA | Message: Missing field'		
    elif not measurement["received"]:
        return '| Status: NO DATA | Message: Communication error'
    elif measurement["value"] is None :
        return '| Status: INVALID DATA | Message: Missing value'
    elif  not isinstance(measurement["value"], (int, float)) or isinstance(measurement["value"], bool):
        return '| Status: INVALID DATA | Message: Invalid value type'    
    elif measurement["value"] > 100 or measurement["value"] < 0:
        return '| Status: OUT OF RANGE | Message: Invalid temperature'
    else:
        return '| Status: OK | Message: Normal'

def summarize_measurements(measurements):
    status = {
        "OK": 0,
        "OUT OF RANGE": 0,
        "NO DATA": 0,
        "INVALID DATA": 0
    }
    for measurement in measurements:
        parts = diagnose_measurement(measurement).split('|')
        status_name = parts[1].strip().replace("Status: ", "")
        if status_name == 'OK':
            status['OK']=status['OK']+1
        elif status_name == 'OUT OF RANGE':
            status['OUT OF RANGE']=status['OUT OF RANGE']+1
        elif status_name == 'NO DATA':
            status['NO DATA']=status['NO DATA']+1
        elif status_name == 'INVALID DATA':
            status['INVALID DATA']=status['INVALID DATA']+1
    return status   