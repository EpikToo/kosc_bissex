import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BissexHistoryComponent } from './bissex-history/bissex-history.component';
import { BissexIndexComponent } from './bissex-index/bissex-index.component';
import { BissexRangeComponent } from './bissex-range/bissex-range.component';
import { BissexYearComponent } from './bissex-year/bissex-year.component';


const routes: Routes = [
    { path: '', component: BissexIndexComponent },
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