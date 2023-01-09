import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { take } from 'rxjs';

@Component({
  selector: 'app-bissex-year',
  templateUrl: './bissex-year.component.html',
  styleUrls: ['./bissex-year.component.scss']
})
export class BissexYearComponent {
  result! : string;
  constructor(private http: HttpClient) {}
  ngOnInit() {
    this.result = "..."
  }

  onSubmit() {
    const tbx = document.getElementById("yeartbx") as HTMLInputElement | null;
    console.log(tbx?.value)
    this.http.get('http://127.0.0.1:8000/bissex_annee/?year='+tbx?.value)
    .pipe(take(1))
    .subscribe(response => {
      console.log(response)
      const key = Object.keys(response) as Array<keyof typeof response>;
      if (String(response[key[3]]) == "true")
      {
        this.result = tbx?.value + " est une année bissextile !";
      }
      else if (String(response[key[3]]) == "false")
      {
        this.result = tbx?.value + " n'est pas une année bissextile.";
      }
      else if (String(response[key[3]]) == "null")
      {
        this.result = String(response[key[4]]);
      }
    });
  }
}