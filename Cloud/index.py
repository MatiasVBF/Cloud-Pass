# Autenticar na Azure
Connect-AzAccount

# Definir variáveis
$resourceGroupName = "MeuGrupoDeRecursos"
$location = "East US"
$vmName = "MinhaVM"
$imagePublisher = "MicrosoftWindowsServer"
$imageOffer = "WindowsServer"
$imageSku = "2019-Datacenter"
$adminUsername = "adminUser"
$adminPassword = "MinhaSenhaSegura123"

# Criar o grupo de recursos
New-AzResourceGroup -Name $resourceGroupName -Location $location

# Criar credenciais de administrador
$securePassword = ConvertTo-SecureString $adminPassword -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential ($adminUsername, $securePassword)

# Criar máquina virtual
New-AzVm `
  -ResourceGroupName $resourceGroupName `
  -Name $vmName `
  -Location $location `
  -ImagePublisher $imagePublisher `
  -ImageOffer $imageOffer `
  -ImageSku $imageSku `
  -Credential $credential

Write-Output "Máquina virtual '$vmName' criada com sucesso!"
