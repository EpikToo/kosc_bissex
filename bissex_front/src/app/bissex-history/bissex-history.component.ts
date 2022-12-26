import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-bissex-history',
  templateUrl: './bissex-history.component.html',
  styleUrls: ['./bissex-history.component.scss']
})
export class BissexHistoryComponent {
  command_type!: string;
  command_entry!: string;
  command_result!: string;
  command_date!: Date;
  command_error!: string;
  constructor(private http: HttpClient) {}

  ngOnInit() {

    this.command_type = "test type";
    this.command_entry = "test entry";
    this.command_result = "test result";
    this.command_date = new Date();
    this.command_error = "test error";

  }

  getData() {
    this.http.get('http://127.0.0.1:8000/bissex_annee/?year=2024')
      .subscribe(data => {
        console.log(data);
      });
  }

  onClickHistory() {
    this.getData()

  }

}

