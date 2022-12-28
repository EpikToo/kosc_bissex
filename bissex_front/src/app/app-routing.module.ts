import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BissexHistoryComponent } from './bissex-history/bissex-history.component';
import { BissexRangeComponent } from './bissex-range/bissex-range.component';
import { BissexYearComponent } from './bissex-year/bissex-year.component';


const routes: Routes = [
    { path: 'history', component: BissexHistoryComponent },
    { path: 'year', component: BissexYearComponent },
    { path: 'range', component: BissexRangeComponent },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {
    
}