import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BissexHistoryComponent } from './bissex-history/bissex-history.component';

@NgModule({
  declarations: [
    AppComponent,
    BissexHistoryComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
