#Luis Alberto Trejo Tovar 1815758

#Script para checar si los servicios que le proporcionas con un txt se esta ejecutando

#De parametros necesita el path del txt y donde se guarda la respuesta



function servicios{
    param([Parameter(Mandatory)] [string] $path,
        [Parameter(Mandatory)][string]$respuesta)
    
    foreach($line in Get-Content -Path $path){
        $servicio = Get-Service -Name $line
        if($servicio.Status -eq "Running"){
            Add-Content -Path $respuesta -Value "Servicio activo: $line " 
        }
    }
    Get-Content -Path $respuesta | Sort-Object
}
servicios
