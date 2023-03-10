import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { take } from 'rxjs/operators';


@Component({
  selector: 'app-bissex-history',
  templateUrl: './bissex-history.component.html',
  styleUrls: ['./bissex-history.component.scss']
})
export class BissexHistoryComponent {
  history_row! : string;
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.onClickHistory();
  }

  onClickHistory() {
    this.http.get('http://0.0.0.0:8000/bissex_history/')
    .pipe(take(1))
    .subscribe(response => {
      const keys = Object.keys(response) as Array<keyof typeof response>;
      this.history_row = "";      
      for(var i in keys){
        var nested  = Object.keys(response[keys[i]]) as Array<keyof typeof response>;
        this.history_row += '<div class="row">';
        this.history_row += '<div class="col-sm"><p>' + keys[i] + '</p></div>';
        for(var u in nested){
          this.history_row += '<div class="col-sm"><p>' + response[keys[i]][nested[u]] + '</p></div>';
        }
        this.history_row += '</div></br>';
      }
    });
  }
}