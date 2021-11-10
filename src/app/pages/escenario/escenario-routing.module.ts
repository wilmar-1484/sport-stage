import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { EscenarioPage } from './escenario.page';

const routes: Routes = [
  {
    path: '',
    component: EscenarioPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class EscenarioPageRoutingModule {}
