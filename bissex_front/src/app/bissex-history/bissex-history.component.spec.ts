import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BissexHistoryComponent } from './bissex-history.component';
import { HttpClientTestingModule, HttpTestingController} from '@angular/common/http/testing';

describe('BissexHistoryComponent', () => {
  let component: BissexHistoryComponent;
  let HttpMock: HttpTestingController;
  let fixture: ComponentFixture<BissexHistoryComponent>;

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [ BissexHistoryComponent ],
      imports: [HttpClientTestingModule],
    })
    .compileComponents();
    HttpMock = TestBed.get(HttpTestingController);
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BissexHistoryComponent);
    component = fixture.componentInstance;
  });
  
  it('bissex_history: should make an HTTP GET request, and change DOM with properly disposed history', (() => { 
    component.onClickHistory();
    const req = HttpMock.expectOne('http://0.0.0.0:8000/bissex_history');
    expect(req.request.method).toEqual('GET');
    req.flush({"10/01/2023 08:28:32":[["Bissex_Range"],["2020 - 2030"],["[2020, 2024, 2028]"],["OK"]]});
    HttpMock.verify();
    expect(component.history_row).toEqual('<div class="row"><div class="col-sm"><p>10/01/2023 08:28:32</p></div><div class="col-sm"><p>Bissex_Range</p></div><div class="col-sm"><p>2020 - 2030</p></div><div class="col-sm"><p>[2020, 2024, 2028]</p></div><div class="col-sm"><p>OK</p></div></div></br>');
  }));
});
