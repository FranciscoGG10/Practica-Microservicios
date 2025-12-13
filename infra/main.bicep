param location string = resourceGroup().location
param appServicePlanName string = 'myAppServicePlan'
param webAppName string = 'myWebApp'
param containerImageAuth string = 'your_auth_service_image:latest'
param containerImageGame string = 'your_game_service_image:latest'
param containerImageScore string = 'your_score_service_image:latest'
param containerImageFrontend string = 'your_frontend_image:latest'

resource appServicePlan 'Microsoft.Web/serverfarms@2021-02-01' = {
  name: appServicePlanName
  location: location
  sku: {
    Tier: 'Standard'
    Size: 'S1'
  }
}

resource webAppAuth 'Microsoft.Web/sites@2021-02-01' = {
  name: '${webAppName}-auth'
  location: location
  kind: 'app'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'DOCKER|${containerImageAuth}'
    }
  }
}

resource webAppGame 'Microsoft.Web/sites@2021-02-01' = {
  name: '${webAppName}-game'
  location: location
  kind: 'app'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'DOCKER|${containerImageGame}'
    }
  }
}

resource webAppScore 'Microsoft.Web/sites@2021-02-01' = {
  name: '${webAppName}-score'
  location: location
  kind: 'app'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'DOCKER|${containerImageScore}'
    }
  }
}

resource webAppFrontend 'Microsoft.Web/sites@2021-02-01' = {
  name: '${webAppName}-frontend'
  location: location
  kind: 'app'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'DOCKER|${containerImageFrontend}'
    }
  }
}