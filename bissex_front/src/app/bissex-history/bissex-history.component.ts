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
  command_type!: string;
  command_entry!: string;
  command_result!: string;
  command_date!: Date;
  command_error!: string;
  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.onClickHistory()
    this.history = ""
    this.command_type = "test type";
    this.command_entry = "test entry";
    this.command_result = "test result";
    this.command_date = new Date();
    this.command_error = "test error";
  }

  

  onClickHistory() {
    this.http.get('http://127.0.0.1:8000/bissex_history')
    .pipe(take(1))
    .subscribe(response => {
      const keys = Object.keys(response) as Array<keyof typeof response>;
      for(var i in keys){
        this.history += keys[i] + '<br/>';
      }
    });
  }
}

