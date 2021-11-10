import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { EscenarioPageRoutingModule } from './escenario-routing.module';

import { EscenarioPage } from './escenario.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    EscenarioPageRoutingModule
  ],
  declarations: [EscenarioPage]
})
export class EscenarioPageModule {}
