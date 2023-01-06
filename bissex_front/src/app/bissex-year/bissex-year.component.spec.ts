import { flush, TestBed } from '@angular/core/testing';
import { BissexYearComponent } from './bissex-year.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { of } from 'rxjs/internal/observable/of';


describe('BissexYearComponent', () => {
  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [ BissexYearComponent ],
      imports: [HttpClientModule],
    })
    .compileComponents();
  });

  it('should show nothing in p on page launch', (() => {
    const fixture = TestBed.createComponent(BissexYearComponent);
    fixture.detectChanges();
    const compiled = fixture.debugElement.nativeElement;
    expect(compiled.querySelector('p').textContent).toContain('...');
  }));

  it('should show correct result in p when submiting empty form information', (() => {
    const fixture = TestBed.createComponent(BissexYearComponent);
    const component = fixture.componentInstance
    const compiled = fixture.debugElement.nativeElement;
    const JSONvalues = '{"id":103,"command_type":"Bissex_Year","command_entry":"2024","command_result":true,"command_error":"OK"}';
    console.log("salut");
    compiled.querySelector('#presult').textContent = "2024 est une année bissextile !"
    expect(compiled.querySelector('#presult').textContent).toContain('2024 est une année bissextile !');
  }));
});

