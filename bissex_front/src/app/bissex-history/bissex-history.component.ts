import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { take } from 'rxjs/operators';


@Component({
  selector: 'app-bissex-history',
  templateUrl: './bissex-history.component.html',
  styleUrls: ['./bissex-history.component.scss']
})
export class BissexHistoryComponent {
  history! : string;
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.onClickHistory()
    this.history = ""
  }

  onClickHistory() {
    this.http.get('http://127.0.0.1:8000/bissex_history')
    .pipe(take(1))
    .subscribe(response => {
      const keys = Object.keys(response) as Array<keyof typeof response>;
      for(var i in keys){
        this.history += keys[i] + ": ";
        var nested  = Object.keys(response[keys[i]]) as Array<keyof typeof response>;
        for(var u in nested){
          this.history += " " + response[keys[i]][nested[u]];
        }
        this.history += '<br/>'
      }
    });
  }
}

