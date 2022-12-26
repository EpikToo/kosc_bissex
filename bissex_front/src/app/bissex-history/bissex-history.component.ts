import { Component } from '@angular/core';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';


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

  ngOnInit() {

    this.command_type = "test type";
    this.command_entry = "test entry";
    this.command_result = "test result";
    this.command_date = new Date();
    this.command_error = "test error";

  }
  /**
  onClickHistory() {
    this.command_type = http.get(this.configUrl);

  }

  HTTPGet(){
    // 👇️ const response: Response
    const response = fetch('https://reqres.in/api/users', {
      method: 'GET',
      headers: {
        Accept: 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`Error! status: ${response.status}`);
    }

    // 👇️ const result: GetUsersResponse
    const result = (response.json());

    console.log('result is: ', JSON.stringify(result, null, 4));

    return result;
  }
  */
}
