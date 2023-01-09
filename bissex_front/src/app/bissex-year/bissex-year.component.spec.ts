import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BissexYearComponent } from './bissex-year.component';
import { HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';
import { By } from '@angular/platform-browser';

describe('BissexYearComponent', () => {
  let component: BissexYearComponent;
  let HttpMock: HttpTestingController;
  let fixture: ComponentFixture<BissexYearComponent>;
  

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [ BissexYearComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();
    HttpMock = TestBed.get(HttpTestingController);
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BissexYearComponent);
    component = fixture.componentInstance;
  });

  it('should make an HTTP GET request, and change DOM', (() => {
    const yeartbxDebugElement = fixture.debugElement.query(By.css('#yeartbx'));
    const yeartbx = yeartbxDebugElement.nativeElement as HTMLInputElement;
    yeartbx.value = "2024"
    component.onSubmit();
    const req = HttpMock.expectOne('http://127.0.0.1:8000/bissex_annee/?year=2024');
    expect(req.request.method).toEqual('GET');
    req.flush({"id":139,"command_type":"Bissex_Year","command_entry":"2024","command_result":true,"command_error":"OK"});
    HttpMock.verify();
    expect(component.result).toEqual('2024 est une année bissextile !');
  }));
});

