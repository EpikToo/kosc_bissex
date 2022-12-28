import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BissexHistoryComponent } from './bissex-history/bissex-history.component';

import { HttpClientModule } from '@angular/common/http';
import { BissexYearComponent } from './bissex-year/bissex-year.component';
import { BissexRangeComponent } from './bissex-range/bissex-range.component';
import { BissexIndexComponent } from './bissex-index/bissex-index.component';
import { AppRoutingModule } from './app-routing.module';
import { BissexBannerComponent } from './bissex-banner/bissex-banner.component';


@NgModule({
  declarations: [
    AppComponent,
    BissexHistoryComponent,
    BissexYearComponent,
    BissexRangeComponent,
    BissexIndexComponent,
    BissexBannerComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { 
  
}

